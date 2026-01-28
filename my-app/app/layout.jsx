
'use client';


import Link from 'next/link';
import './globals.css';

const MainLayout = ({ children }) => {

  return (
    <html lang="en">
      <head>
        <title>Main Layout</title>
      </head>
      <body>


        {/* Main Content */}
        <main>
          {children}
        </main>

      </body>
    </html >
  );
}

export default MainLayout;