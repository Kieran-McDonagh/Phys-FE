import axios, { AxiosRequestConfig } from "axios";
import { BASE_URL } from "../baseUrl";

async function deleteWorkoutData(workoutId: string, accessToken: string, tokenType: string) {
  try {
    const config: AxiosRequestConfig = {
      headers: {
        Authorization: `${tokenType} ${accessToken}`,
      },
    };
    await axios.delete(
        `${BASE_URL}/api/workouts/${workoutId}`,
        config
      );
  } catch (error) {
    console.error(`Error handling delete request from API: ${error}`)
  }
}

export default deleteWorkoutData