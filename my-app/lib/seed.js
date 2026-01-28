import { db } from './db.js';
import { users } from '../models/User.js';

async function seed() {
    try {
        console.log('Seeding database...');

        // Insert test users
        const testUsers = await db.insert(users).values([
            {
                id: '1',
                email: 'john.doe@example.com',
                username: 'johndoe',
                name: 'John Doe',
                image: 'https://i.pravatar.cc/150?img=1',
                bio: 'Software developer and coffee enthusiast',
            },
            {
                id: '2',
                email: 'jane.smith@example.com',
                username: 'janesmith',
                name: 'Jane Smith',
                image: 'https://i.pravatar.cc/150?img=2',
                bio: 'Designer and creative thinker',
            },
            {
                id: '3',
                email: 'bob.wilson@example.com',
                username: 'bobwilson',
                name: 'Bob Wilson',
                image: 'https://i.pravatar.cc/150?img=3',
                bio: 'Tech lead and open source contributor',
            },
        ]).returning();

        console.log('✅ Successfully added test users:');
        console.log(testUsers);
    } catch (error) {
        console.error('❌ Error seeding database:', error);
    }
}

seed();
