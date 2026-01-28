import Database from 'better-sqlite3';
import { drizzle } from 'drizzle-orm/better-sqlite3';
import { users } from '../models/User.js';

const sqlite = new Database('sqlite.db');
export const db = drizzle(sqlite, { schema: { users } });

export default {
    schema: './models/*',
    out: './drizzle',
    driver: 'better-sqlite3',
    dbCredentials: {
        url: 'sqlite.db',
    },
};