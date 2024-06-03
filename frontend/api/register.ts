import axios from "axios";

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
  data: UserData;
}

async function sendRegisterData(
  email: string,
  username: string,
  full_name: string,
  password: string
): Promise<LoginResponse> {
  const userData = {
    email,
    username,
    full_name,
    password,
  };
  try {
    const response = await axios.post<LoginResponse>("http://0.0.0.0:8000/api/users", userData);
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

export default sendRegisterData;
