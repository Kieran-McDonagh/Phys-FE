import axios, { AxiosRequestConfig } from "axios";
import { BASE_URL } from "./base-url";

interface WorkoutData {
  id: string;
  type: string;
  title: string;
  body: Record<string, any>;
  notes: string;
  user_id: string;
  date_created: string;
}

async function getUserWorkoutData(id: string, accessToken: string, tokenType: string): Promise<WorkoutData[]> {
  try {
    const config: AxiosRequestConfig = {
      headers: {
        Authorization: `${tokenType} ${accessToken}`,
      },
    };

    const response = await axios.get<WorkoutData[]>(`${BASE_URL}/api/workouts?user_id=${id}`, config);
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

export default getUserWorkoutData;
