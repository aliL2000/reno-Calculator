import Head from "next/head";
import styles from "../styles/Home.module.css";
import { Button } from "@mui/material";
import Link from "next/link";
import Layout from "../components/layout";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Reno-Calculator</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Layout>
      <main>
        <h1 className={styles.title}>Reno-Calculator</h1>

        <section className="user-inputting">
          <p className={styles.description}>I want to:</p>
          <div className={styles.grid}>
            <Link href="/home/options" className={styles.card}>
              <h3>BUY</h3>
              <p className={styles.cardDescription}>my home</p>
            </Link>
            <Link href="/renovation/options" className={styles.card}>
              <h3>RENOVATE</h3>
              <p className={styles.cardDescription}>my home</p>
            </Link>
          </div>
        </section>

        <section className="price-explanation">
          <div>
            <h3 className={styles.subtitle}>
              Knowledge is priceless - so our renovation cost pricing is free.
            </h3>
            <div className={styles.grid}>
              <p>
                Always know what to expect from a home renovation with our cost
                guides. From materials to labour, we have the data-backed info
                you need as a homeowner to start with confidence.
              </p>
              <img
                src="/form.png"
                alt="Cost Estimation Image"
                className={styles.costScreenshot}
              />
            </div>
          </div>
        </section>


      </main>
      </Layout>

      <style jsx>{`
        main {
          padding: 5rem 0;
          flex: 1;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
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

    </div>
  );
}
