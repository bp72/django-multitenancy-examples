This is an example of multi-tenant app with shared database and separate schema.
It has a `Tenant` model where the application tenants can be defined. And all other models are linked to `Tenant` via the foreign key.
The `Tenant` model has `host` field that will be used to identify, which tenant is requesting the data at the moment.

# How to run an example

1. Go to `02_shared_database_separate_schema` directory and run:

```bash
docker-compose up
```

2. Open django admin site using username `admin` and password `admin`: http://127.0.0.1:8000/admin/
3. Ensure that the application works and there is sample data in the database.
4. Run the following requests to see how the filtering works:

For Tenant #1:

```bash
curl http://127.0.0.1:8000/polls/ -H 'Host: tenant1.com'
```

For Tenant #2:

```bash
curl http://127.0.0.1:8000/polls/ -H 'Host: tenant2.com'
```

Check that the data is different and tenants don't see each other's data.