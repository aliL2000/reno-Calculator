import Head from "next/head";
import styles from "../styles/Home.module.css";
import { Button } from "@mui/material";
import Link from "next/link";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Reno-Calculator</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className={styles.title}>How much will my Home Renovation cost?</h1>

        <p className={styles.description}>Select your options below</p>

        <div className={styles.grid}>
          <Link href="/home/options" className={styles.card}>
            <h3>Full Home</h3>
          </Link>
          <Link href="/renovation/options" className={styles.card}>
            <h3>Bathroom</h3>
          </Link>
          <Link href="/renovation/options" className={styles.card}>
            <h3>Kitchen</h3>
          </Link>
          <Link href="/renovation/options" className={styles.card}>
            <h3>Basement</h3>
          </Link>
          <Link href="/renovation/options" className={styles.card}>
            <h3>Add 2nd Floor</h3>
          </Link>
          <Link href="/renovation/options" className={styles.card}>
            <h3>Rear Extension</h3>
          </Link>
          <Link href="/renovation/options" className={styles.card}>
            <h3>Carport Garage</h3>
          </Link>
          <Link href="/renovation/options" className={styles.card}>
            <h3>Exterior</h3>
          </Link>
        </div>

        <div>
          <h3 className={styles.subtitle}>Knowledge is priceless - so our renovation cost pricing is free.</h3>
          <div className={styles.grid}>
            <p>Always know what to expect from a home renovation with our cost guides. From materials to labour, we have the data-backed info you need as a homeowner to start with confidence.</p>
            <img src="/vercel.svg" alt="Cost Estimation Image" className={styles.logo} />
          </div>
        </div>

        <div>
          <h3 className={styles.subtitle}>Get free project cost information delievered to your mailbox.</h3>
          <div className={styles.grid}>
            <p>Always know what to expect from a home renovation with our cost guides. From materials to labour, we have the data-backed info you need as a homeowner to start with confidence.</p>
            <img src="/vercel.svg" alt="Cost Estimation Image" className={styles.logo} />
          </div>
        </div>

      </main>

      <footer>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{" "}
          <img src="/vercel.svg" alt="Vercel" className={styles.logo} />
        </a>
      </footer>

      <style jsx>{`
        main {
          padding: 5rem 0;
          flex: 1;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        footer {
          width: 100%;
          height: 100px;
          border-top: 1px solid #eaeaea;
          display: flex;
          justify-content: center;
          align-items: center;
        }
        footer img {
          margin-left: 0.5rem;
        }
        footer a {
          display: flex;
          justify-content: center;
          align-items: center;
          text-decoration: none;
          color: inherit;
        }
        code {
          background: #fafafa;
          border-radius: 5px;
          padding: 0.75rem;
          font-size: 1.1rem;
          font-family: Menlo, Monaco, Lucida Console, Liberation Mono,
            DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace;
        }
      `}</style>

      <style jsx global>{`
        html,
        body {
          padding: 0;
          margin: 0;
          font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
            Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue,
            sans-serif;
        }
        * {
          box-sizing: border-box;
        }
      `}</style>
    </div>
  );
}
