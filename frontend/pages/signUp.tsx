import Link from "next/link";
import Head from "next/head";

export default function signUp() {
  return (
    <>
      <Head>
        <title>Project Estimation Explained</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h1>Sign Up</h1>
      <h2>
        <Link href="/">Back to home</Link>
      </h2>
    </>
  );
}
