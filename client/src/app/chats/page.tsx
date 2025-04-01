import styles from './chats.module.scss';
import { redirect } from 'next/navigation'
import { auth } from '@/auth'
import ChatCard from '../components/ChatCard/ChatCard'

interface IChat {
    id: string;
    name: string;
    message: string;
    time: string;
}

const Chats = async () => {
  const session = await auth()
  const user = session?.user

  if(!user) {
    redirect('/')
  }

  const chats: IChat[] = [
      { id: '1000', name: 'John Doe', message: 'Hey there!', time: '4m' },
      { id: '1001', name: 'Jane Doe', message: 'Hello!', time: '1h' },
    ]

  return (
    <div className={styles.page}>
      <div className={styles.title}>Chats</div>
      {
        chats.map((chat) => (
          <ChatCard key={chat.id} chat={chat} />
        ))
      }
    </div>
  )
}

export default Chats 
