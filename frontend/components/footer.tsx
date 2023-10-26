import React from "react";
import styles from "./layout.module.css";
import Link from "next/link";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <section className={styles.footerSignUp}>
        <div>
          <h3>ARE YOU A HOMEOWNER?</h3>
        </div>
        <div>
          <h3>ARE YOU A CONTRACTOR?</h3>
        </div>
      </section>
      <section className={styles.footerInfo}>
        <div>
          <h3>Homeowner</h3>
          <Link href={'./'}>
            Renovation Cost Calculator
          </Link>
        </div>
        <div>
          <h3>Contractor</h3>
          <Link href={'./'}>
            Register your business
          </Link>
          <Link href={'./'}>
            Guidelines
          </Link>
        </div>
        <div>
          <h3>Learn</h3>
          <Link href={'./'}>
            Project Costs Explained
          </Link>
          <Link href={'./'}>
            FAQ's
          </Link>
        </div>
        <div>
          <h3>About Us</h3>
          <Link href={'./'}>
            How it works
          </Link>
          <Link href={'./'}>
            Who we are
          </Link>
          <Link href={'./'}>
            Contact Us
          </Link>
          <Link href={'./'}>
            Happiness Gaurantee
          </Link>
        </div>
      </section>
      
    </footer>
  );
};

export default Footer;
