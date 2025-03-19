import Link from 'next/link'
import styles from '@/app/components/Navbar.module.scss'
import { Home, MessageCircle, Settings } from "lucide-react";


const Navbar = () => {
  return (
    <div className={styles.container}>
      <Link href="/" className={styles.logo}>LOGO</Link>
      <ul>
        <li className={styles.li}> 
          <Link className={styles.link} href="/home">
            <MessageCircle className={styles.icon}/>
            <p>All Chats</p>
          </Link>
        </li>
        <li className={styles.li}> 
          <Link className={styles.link} href="/">
            <Settings className={styles.icon} />
            <p>Settings</p>
          </Link>
        </li>
      </ul> 
    </div>
  )
}

export default Navbar
