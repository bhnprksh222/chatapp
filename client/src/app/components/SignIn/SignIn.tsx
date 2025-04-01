import styles from '../SignIn/SignIn.module.scss'
import { auth, signIn } from '@/auth'

export default async function SignIn() {
  const session = await auth()
  const user = session?.user

  return !user && (
    <form
      action={async () => {
        "use server"
        await signIn("google")
      }}
    > 
      <button type='submit'>Sign In with Google</button>
    </form> 
)}

