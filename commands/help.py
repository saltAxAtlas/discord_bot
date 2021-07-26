async def execute(message, vars):
	if len(message.content.split()) == 2:
		_, command = message.content.split()
		cmds = vars['commands']
		for cmd in cmds:
			if command == cmd['command'] or command in cmd['aliases']:
				cmd_info = {
					'Name': f'{vars["command_prefix"]}{cmd["command"]}',
					'Aliases': ', '.join(f'{vars["command_prefix"]}{alias}' for alias in cmd['aliases']),
					'Description': cmd['description']
				}
				maxlen = max(map(len, cmd_info.keys()))
				resp = f'Information About {vars["command_prefix"]}{command}'
				for key, value in cmd_info.items():
					resp += f'\n`{key.ljust(maxlen)}`: {value}'
				return await message.channel.send(resp.strip())
		else:
			return await message.channel.send(f'{command} is not a valid command!')
	else:
		resp = 'Try $commands for a simplified command list.\n'
		cmds = vars['commands']
		maxlen = len(str(len(cmds)+1))
		for idx, val in enumerate(cmds):
			resp += f'\t`{str(idx+1).rjust(maxlen)}`. {vars["command_prefix"]}{val["command"]} - {val["description"]}\n'
		return await message.channel.send(resp.strip())

cmd = {
	'command': 'help',
	'aliases': [],
	'description': 'an in-depth explanation of the available commands.',
	'run': execute
}
