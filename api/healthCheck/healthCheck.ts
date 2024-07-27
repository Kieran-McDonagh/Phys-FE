import axios from "axios";
import { BASE_URL } from "../baseUrl";

interface HealthCheckData {
    status: string;
    code: number;
}

type HealthCheckResponse = [string, number];

async function apiHealthCheck(): Promise<HealthCheckData | undefined> {
    try {
        const result = await axios.get<HealthCheckResponse>(`${BASE_URL}/healthcheck`);
        const [status, code] = result.data;
        return { status, code };
    } catch (error) {
        console.log(`Error requesting health check from api: ${error}`);
        return undefined;
    }
}

export default apiHealthCheck;
