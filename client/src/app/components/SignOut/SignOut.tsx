import { auth, signOut } from '@/auth'
import { redirect } from 'next/navigation'

const SignOut = async () => {
  const session = await auth()
  const user = session?.user
  return (
      <form
        action={ async () => {
            "use server"
            await signOut() 
        }}
      >
        <button>Sign Out</button>
      </form>
  )
}

export default SignOut
