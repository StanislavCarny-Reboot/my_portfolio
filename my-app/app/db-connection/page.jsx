import { db } from '@/lib/db';
import { users } from '@/models/User';

const UsersPage = async () => {

    const allUsers = await db.select().from(users);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-3xl font-bold mb-6">Database Users</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {allUsers.map((user) => (
                    <div key={user.id} className="border rounded-lg p-4 shadow-md">
                        {user.image && (
                            <img
                                src={user.image}
                                alt={user.name || user.username}
                                className="w-20 h-20 rounded-full mx-auto mb-3"
                            />
                        )}
                        <h3 className="text-xl font-semibold text-center">{user.name}</h3>
                        <p className="text-gray-600 text-center">@{user.username}</p>
                        <p className="text-sm text-gray-500 text-center mt-2">{user.email}</p>
                        {user.bio && (
                            <p className="text-sm mt-3 text-center">{user.bio}</p>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );

}

export default UsersPage;   