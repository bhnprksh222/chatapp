"use client"

import { useRouter } from 'next/navigation';
import styles from './ChatCard.module.scss';

interface IChat {
  id: string;
  name: string;
  message: string;
  time: string;
};

export default function ChatCard({chat}: { chat: IChat}) {
  const router = useRouter();

  const handleClick = () => {
    router.push(`/chats/${chat.id}`);
  };

  return (
    <div className={styles.chat} onClick={handleClick}>
      <div className={styles.chatImage}>
        <img
          src="https://wallpapersok.com/images/hd/cool-neon-blue-profile-picture-u9y9ydo971k9mdcf.jpg"
          alt="Picture of the author"
        />
      </div>
      <div className={styles.chatInfo}>
        <div className={styles.chatInfoTop}>
          <div className={styles.chatInfoTopName}>{chat.name}</div>
          <div className={styles.chatInfoTopTime}>{chat.time}</div>
        </div>
        <div className={styles.chatInfoMessage}>{chat.message}</div>
      </div>
    </div>
  );
}
