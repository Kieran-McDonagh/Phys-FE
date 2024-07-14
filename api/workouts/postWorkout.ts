import axios, { AxiosRequestConfig } from "axios";
import { BASE_URL } from "../baseUrl";

interface WorkoutData {
  type: string;
  title: string;
  body: string;
  notes: string;
}

interface ReturnedWorkoutData {
  id: string;
  type: string;
  title: string;
  body: Record<string, any>;
  notes: string;
  user_id: string;
  date_created: string;
}

async function postWorkoutData(
  workoutData: WorkoutData,
  accessToken: string,
  tokenType: string
): Promise<ReturnedWorkoutData> {
  try {
    const config: AxiosRequestConfig = {
      headers: {
        Authorization: `${tokenType} ${accessToken}`,
      },
    };
    const response = await axios.post<ReturnedWorkoutData>(
      `${BASE_URL}/api/workouts`,
      workoutData,
      config
    );
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error("Error message: ", error.message);
      if (error.response) {
        console.error("Error response data: ", error.response.data);
      }
    } else {
      console.error("Unexpected error: ", error);
    }
    throw error;
  }
}

export default postWorkoutData;
