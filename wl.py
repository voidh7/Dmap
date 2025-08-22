wordlist = [
# Admin panels
"/admin", "/admin.php", "/admin/login.php", "/admin/dashboard.php", "/admin/config.php", "/admin/settings.php",                             "/administrator", "/cpanel", "/manager", "/manager/html", "/xp-admin", "/login", "/signin", "/logout",
"/auth.php", "/register.php", "/reset-password", "/forgot-password", "/dashboard", "/controlpanel", "/panel",
"/admin_area", "/backend", "/system", "/console", "/admin_console", "/root", "/superadmin", "/adm",

# Sensitive scripts and files
"/config.php", "/config.js", "/settings.php", "/core.php", "/app.js", "/index.js", "/main.js",
"/phpinfo.php", "/info.php", "/install.php", "/update.php", "/upgrade.php", "/init.php",
"/bootstrap.php", "/autoload.php", "/composer.json", "/package.json", "/setup.php", "/maintenance.php",
"/env.php", "/routes.php", "/database.php", "/db.php",

# Hidden directories and files
"/.git", "/.git/config", "/.env", "/.htaccess", "/.htpasswd", "/.DS_Store", "/.svn", "/.idea",
"/logs", "/log", "/tmp", "/temp", "/backup", "/old", "/test", "/tests", "/dev", "/private", "/secret",
"/hidden", "/cache", "/sessions", "/sessions.php", "/uploads/tmp", "/uploads/backups",

# Database and backups
"/db", "/database", "/sql", "/backup.sql", "/database.sql", "/dump.sql", "/mysql", "/phpmyadmin", "/pma", "/sqladmin",
"/db_backup", "/db.sql", "/data.sql", "/export.sql", "/mysql_dump", "/db_dump.sql", "/backup_db",

# APIs and endpoints
"/api", "/api/v1", "/api/v2", "/ajax", "/ajax.php", "/rest", "/graphql", "/webhook", "/endpoint", "/service",
"/api/admin", "/api/auth", "/api/login", "/api/user", "/api/data", "/api/config", "/api/update",

# Public files that may leak info
"/robots.txt", "/sitemap.xml", "/license.txt", "/readme.html", "/CHANGELOG.md", "/composer.json", "/package.json",
"/vendor", "/includes", "/inc", "/lib", "/modules", "/extensions", "/docs", "/documentation", "/manual",
"/help", "/info", "/about", "/changelog", "/history", "/version", "/versions", "/release_notes",

# Media and uploads
"/upload", "/uploads", "/files", "/media", "/images", "/img", "/assets", "/attachments",
"/images/tmp", "/uploads/images", "/uploads/files", "/uploads/docs", "/media/images", "/media/files",

# Common frameworks and CMS
"/wp-admin", "/wp-login.php", "/wp-content", "/wp-includes",
"/joomla/administrator", "/drupal/admin", "/modx/manager",
"/prestashop/admin", "/shopware/backend", "/magento/admin",
"/typo3/typo3", "/laravel/public", "/cakephp/app", "/symfony/app",
"/codeigniter/admin", "/django/admin", "/flask/admin", "/rails/admin",

# Common exploits and test scripts
"/index.php?id=1", "/index.php?cat=1", "/search.php?q=test", "/eval.php", "/test.php", "/debug.php",
"/sql.php", "/upload.php", "/file_upload.php", "/download.php", "/get.php", "/fetch.php",
"/check.php", "/verify.php", "/validate.php", "/confirm.php",

# Generic sensitive directories
"/core", "/core/includes", "/core/modules", "/core/lib", "/core/config",
"/system", "/system/config", "/system/logs", "/system/temp",
"/app", "/app/config", "/app/cache", "/app/logs", "/app/tmp",
"/private", "/private/config", "/private/data", "/private/backups",
"/backup", "/backup/db", "/backup/files", "/backup/scripts",
"/test", "/testing", "/sandbox", "/sandbox/tmp", "/demo", "/staging",

# Additional script endpoints
"/run.php", "/start.php", "/init.php", "/process.php", "/execute.php",
"/shell.php", "/cmd.php", "/command.php", "/terminal.php",
"/ajax-handler.php", "/api-handler.php", "/service.php", "/worker.php",

# Configuration files
"/.npmrc", "/.yarnrc", "/.babelrc", "/.eslintrc", "/.prettierrc",
"/docker-compose.yml", "/Dockerfile", "/Makefile", "/Gruntfile.js", "/Gulpfile.js",

# Logs and history files
"/access.log", "/error.log", "/debug.log", "/app.log", "/system.log",
"/activity.log", "/trace.log", "/events.log", "/user.log",

# User directories
"/users", "/members", "/accounts", "/profiles", "/clients", "/customers",
"/data/users", "/data/members", "/data/accounts", "/data/profiles",

# Old files and backups
"/old", "/old_site", "/old_files", "/old_backup", "/archive", "/archives",
"/tmp_backup", "/temp_backup", "/backup_old", "/backup_archive",

# Miscellaneous
"/favicon.ico", "/robots.txt", "/sitemap.xml", "/humans.txt", "/ads.txt",
"/mail", "/mailer", "/newsletter", "/contact", "/support", "/helpdesk"
] 