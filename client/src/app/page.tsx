import SignIn from "@/app/components/SignIn/SignIn";
import styles from  "./page.module.scss";

const Home = () => {
  return (
    <div>
        {/*
          TODO:
          Add logic to display logo when page loads
          once logged in should display some greeting text
        */}
        <p className={styles.test}>WAVEY</p>
        <SignIn />
    </div>
  )
}

export default Home
