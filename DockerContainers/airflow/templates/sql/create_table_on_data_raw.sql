CREATE TABLE if not exists devel.clients (
	id varchar NULL,
	"name" varchar NULL,
	execution_ts timestamp NULL DEFAULT CURRENT_TIMESTAMP
);