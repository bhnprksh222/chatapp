'use client'
import styles from './chats.module.scss';
import { useRouter } from 'next/navigation'

const Chats = () => {
  const router = useRouter();

  const handleClickOnChat = () => {
    router.push('/chats/${chatId}')
  } 

  return (
    <div className={styles.chats}>
      <div className={styles.title}>Chats</div>
      <div
        className={styles.chat} 
        id="1000"
        onClick={() => handleClickOnChat}
      >
        <div className={styles.chatImage}>
          <img src="https://wallpapersok.com/images/hd/cool-neon-blue-profile-picture-u9y9ydo971k9mdcf.jpg" alt="Picture of the author" />
        </div>
        <div className={styles.chatInfo}>
          <div className={styles.chatInfoTop}>
            <div className={styles.chatInfoTopName}>Name</div>
            <div className={styles.chatInfoTopTime}>4m</div>
          </div>
          <div className={styles.chatInfoMessage}>message</div>
        </div>
      </div> 
      {/*<div className={styles.chat}>
        <div className={styles.chatImage}>
          <img src="https://wallpapersok.com/images/hd/cool-neon-blue-profile-picture-u9y9ydo971k9mdcf.jpg" alt="Picture of the author" />
        </div>
        <div className={styles.chatInfo}>
          <div className={styles.chatInfoTop}>
            <div className={styles.chatInfoTopName}>Name</div>
            <div className={styles.chatInfoTopTime}>4m</div>
          </div>
          <div className={styles.chatInfoMessage}>message</div>
        </div>
      </div> 
      <div className={styles.chat}>
        <div className={styles.chatImage}>
          <img src="https://wallpapersok.com/images/hd/cool-neon-blue-profile-picture-u9y9ydo971k9mdcf.jpg" alt="Picture of the author" />
        </div>
        <div className={styles.chatInfo}>
          <div className={styles.chatInfoTop}>
            <div className={styles.chatInfoTopName}>Name</div>
            <div className={styles.chatInfoTopTime}>4m</div>
          </div>
          <div className={styles.chatInfoMessage}>message</div>
        </div>
      </div> 
      */}
    </div>
  )
}

export default Chats 
