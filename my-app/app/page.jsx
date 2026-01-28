import Link from 'next/link';

const HomePage = async () => {
  // Fetch all users from the database


  return (
    <div className="container mx-auto p-4">
      {/* Icon Grid */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 mt-8">
        {/* Database Connection Icon */}
        <Link
          href="/db-connection"
          className="flex flex-col items-center justify-center p-8 bg-white rounded-lg shadow-lg hover:shadow-xl transition border-2 border-gray-200 hover:border-blue-500"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-16 h-16 text-blue-600 mb-3"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125"
            />
          </svg>
          <span className="text-lg font-semibold text-gray-800">db-connection</span>
        </Link>

        {/* Placeholder for future icons */}
        <div className="flex flex-col items-center justify-center p-8 bg-gray-100 rounded-lg shadow border-2 border-dashed border-gray-300">
          <div className="w-16 h-16 bg-gray-300 rounded-full mb-3"></div>
          <span className="text-lg font-semibold text-gray-400">Coming Soon</span>
        </div>

        <div className="flex flex-col items-center justify-center p-8 bg-gray-100 rounded-lg shadow border-2 border-dashed border-gray-300">
          <div className="w-16 h-16 bg-gray-300 rounded-full mb-3"></div>
          <span className="text-lg font-semibold text-gray-400">Coming Soon</span>
        </div>

        <div className="flex flex-col items-center justify-center p-8 bg-gray-100 rounded-lg shadow border-2 border-dashed border-gray-300">
          <div className="w-16 h-16 bg-gray-300 rounded-full mb-3"></div>
          <span className="text-lg font-semibold text-gray-400">Coming Soon</span>
        </div>
      </div>

    </div>

  );
}

export default HomePage;