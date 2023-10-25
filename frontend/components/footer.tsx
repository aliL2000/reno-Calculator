import React from 'react';
import styles from './layout.module.css';

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className="footer-content">
        <p>&copy; {new Date().getFullYear()} Your Website Name</p>
      </div>
    </footer>
  );
};

export default Footer;