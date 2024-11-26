server = {
	'config': {
		'init': ['init_db<func>'],
		'app_configs': ['TestUser<BaseSettings>', 'DatabaseSettings<BaseSettings>', 'JWTSettings<BaseSettings>', 'EmailSettings<BaseSettings>', 'AppConfigs<BaseSettings>'],
		'database': ['get_db<func>', 'get_redis<func>']
	}
}