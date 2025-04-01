import type { Metadata } from "next";
import { SessionProvider } from "next-auth/react";
import { auth } from '@/auth'
import Navbar from "./components/Navbar/Navbar";
import SignOut from './components/SignOut/SignOut'
import "./styles/globals.scss";


export const metadata: Metadata = {
  title: "Chat App",
  description: "",
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const authenticated = await auth();

  return (
    <html lang="en">
      <body>
        <SessionProvider>
          {authenticated && <Navbar />}
          {authenticated && <SignOut/>}
          {children}
        </SessionProvider>
      </body>
    </html>
  );
}

