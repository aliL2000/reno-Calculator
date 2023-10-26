import React from "react";
import styles from "./layout.module.css";
import Image from "next/image";
import Link from "next/link";

const NavBar = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>
        <img src="/favicon.ico" alt="Logo" />
      </div>
      <ul className={styles.navLinks}>
        <li>
          <Link href="/login">Login</Link>
        </li>
        <li>
          <Link href="/signUp">Sign Up</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
