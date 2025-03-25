"use client";

import Link from 'next/link'
import styles from '@/app/components/Navbar.module.scss'
import { Bell, MessageCircle, Settings, Search } from "lucide-react";
import type { LucideIcon } from 'lucide-react';
import { usePathname } from 'next/navigation';

interface ILinkInfo {
  href: string,
  icon: LucideIcon 
}

const Navbar = () => {
  const path = usePathname();
  const links_info: ILinkInfo[] = [
    {
      href: '/chats',
      icon: MessageCircle
    },
    {
      href: '/search',
      icon: Search
    },
    {
      href: '/notifications',
      icon: Bell
    },
    {
      href: '/options',
      icon: Settings
    },
  ]
  
  return (
    <div className={styles.container}>
      <ul>
        {
          links_info.map(({ href, icon: Icon }, index) => {
          const isActive = path === href;
          return (
            <li key={index} className={isActive ? styles.activeli : styles.li}>
              <Link href={href} className={isActive ? styles.active : styles.link}>
                <Icon className={isActive ? styles.iconActive : styles.icon} />
              </Link>
            </li>
          )})
        }
      </ul> 
    </div>
  )
}

export default Navbar
