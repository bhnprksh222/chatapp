import { Pool } from 'pg'
import PostgresAdapter from '@auth/pg-adapter'

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.NODE_ENV === "production" ? { rejectUnauthorized: false } : false
})

export const adapter = PostgresAdapter(pool)
