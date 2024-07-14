import axios from "axios";
import { BASE_URL } from "./baseUrl";

interface UserData {
  id: string;
  username: string;
  full_name: string;
  email: string;
  disabled: boolean;
  workouts: any[];
  nutrition: any[];
  friends: any[];
}
interface LoginResponse {
  access_token: string;
  token_type: string;
  user_data: UserData;
}

async function sendLoginData(
  username: string,
  password: string
): Promise<LoginResponse> {
  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);

  try {
    const response = await axios.post<LoginResponse>(
      `${BASE_URL}/token`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
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

export default sendLoginData;
