export default {
    dialect: 'sqlite',
    schema: './models/*',
    out: './drizzle',
    dbCredentials: {
        url: 'sqlite.db',
    },
};
