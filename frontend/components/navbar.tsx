import React from 'react';
import styles from './layout.module.css';

const NavBar = () => {
  return (
      <div>
        <p>&copy; {new Date().getFullYear()} Your Website Name</p>
      </div>
  );
};

export default NavBar;