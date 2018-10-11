# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


import six
import click
import json
from importlib import import_module

from utils.config import get_config_path, load_config
from utils.logger import framework_log


def entry_point():
    from mod import MOD_LIST
    from utils.mod_helper import import_mod
    config_path = get_config_path()
    mod_configs = load_config(config_path)['mod']
    for mod_tmp in mod_configs:
        mod_name = mod_tmp['mod_name']
        mod_config = mod_tmp['mod_config']
        print(mod_name, mod_config)
        if not mod_config['enable']:
            continue
        if mod_name in MOD_LIST:
            import_mod('mod.sys_mod_' + mod_name)
        else:
            import_mod(mod_name)
    cli(obj={})

@click.group()
@click.option('-v', '--verbose', count=True)
@click.pass_context
def cli(ctx, verbose):
    ctx.obj["VERBOSE"] = verbose


@cli.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.help_option('-h', '--help')
@click.argument('cmd', nargs=1, type=click.Choice(['list', 'enable', 'disable', 'install', 'uninstall']))
@click.argument('params', nargs=-1)
def mod(cmd, params):
    """
    Mod management command

    Lab mod list \n
    Lab mod install xxx \n
    Lab mod uninstall xxx \n
    Lab mod enable xxx \n
    Lab mod disable xxx \n

    """
    def list(params):
        """
        List all mod configuration
        """
        from colorama import init, Fore
        from tabulate import tabulate
        init()
        mod_config_path = get_config_path()
        mod_configs = load_config(mod_config_path)['mod']

        table = []
        for mod_tmp in mod_configs:
            mod_name = mod_tmp['mod_name']
            mod_config = mod_tmp['mod_config']
            table.append([
                Fore.RESET + mod_name,
                Fore.GREEN + "enable" + Fore.RESET if mod_config['enable'] else Fore.RED + "disabled" + Fore.RESET
            ])

        headers = [
            Fore.CYAN + "name",
            Fore.CYAN + "status" + Fore.RESET
        ]

        print(tabulate(table, headers=headers, tablefmt="psql"))
        print(Fore.LIGHTYELLOW_EX + "You can use `lab mod list/install/uninstall/enable/disable` to manage your mods")

    def install(params):
        """
        Install third-party Mod
        """
        from pip import main as pip_main
        from pip.commands.install import InstallCommand

        params = [param for param in params]

        options, mod_list = InstallCommand().parse_args(params)

        params = ["install"] + params

        for mod_name in mod_list:
            mod_name_index = params.index(mod_name)
            if mod_name.startswith("sys_mod_"):
                print('System Mod can not be installed or uninstalled')
                return
            if "mod_" in mod_name:
                lib_name = mod_name
                mod_name = lib_name.replace("mod_", "")
            else:
                lib_name = "mod_" + mod_name
            params[mod_name_index] = lib_name

        # Install Mod
        pip_main(params)

        # Export config
        mod_config_path = get_config_path()
        mod_configs = load_config(mod_config_path)['mod']
        for mod_tmp in mod_configs:
            mod_name = mod_tmp['mod_name']
            mod_config = mod_tmp['mod_config']
            mod_config['mod'][mod_name] = {}
            mod_config['mod'][mod_name]['enable'] = False

        for mod_name in mod_list:
            mod_config['mod'][mod_name] = {}
            mod_config['mod'][mod_name]['enable'] = False

        with open(mod_config_path, 'w') as json_file:
            json_file.write(json.dumps(mod_config))

        list({})

    def uninstall(params):
        """
        Uninstall third-party Mod
        """

        from pip import main as pip_main
        from pip.commands.uninstall import UninstallCommand

        params = [param for param in params]

        options, mod_list = UninstallCommand().parse_args(params)

        params = ["uninstall"] + params

        for mod_name in mod_list:
            mod_name_index = params.index(mod_name)
            if mod_name.startswith("mod_sys_"):
                print('System Mod can not be installed or uninstalled')
                return
            if "mod_" in mod_name:
                lib_name = mod_name
            else:
                lib_name = "mod_" + mod_name
            params[mod_name_index] = lib_name

        # Uninstall Mod
        pip_main(params)

        # Remove Mod Config
        mod_config_path = get_config_path()
        mod_config = load_config(mod_config_path)['mod']

        for mod_name in mod_list:
            if "mod_" in mod_name:
                mod_name = mod_name.replace("mod_", "")
            del mod_config['mod'][mod_name]

        with open(mod_config_path, 'w') as json_file:
            json_file.write(json.dumps(mod_config))
        list({})

    def enable(params):
        """
        enable mod
        """
        mod_name = params[0]
        if "mod_" in mod_name:
            mod_name = mod_name.replace("mod_", "")

        # check whether is installed
        module_name = "mod_" + mod_name
        try:
            import_module(module_name)
        except ImportError:
            install([module_name])

        mod_config_path = get_config_path()
        mod_config = load_config(mod_config_path)['mod']

        mod_config['mod'][mod_name]['enable'] = True
        with open(mod_config_path, 'w') as json_file:
            json_file.write(json.dumps(mod_config))
        list({})

    def disable(params):
        """
        disable mod
        """
        mod_name = params[0]

        if "mod_" in mod_name:
            mod_name = mod_name.replace("mod_", "")

        mod_config_path = get_config_path()
        mod_config = load_config(mod_config_path)['mod']

        mod_config['mod'][mod_name]['enable'] = False
        with open(mod_config_path, 'w') as json_file:
            json_file.write(json.dumps(mod_config))
        list({})

    locals()[cmd](params)


if __name__ == '__main__':
    entry_point()
