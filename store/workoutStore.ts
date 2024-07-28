import { create } from "zustand";
import getUserWorkoutData from "@/api/workouts/getWorkout";
import postWorkoutData from "@/api/workouts/postWorkout";
import deleteWorkoutData from "@/api/workouts/deleteWorkout";

interface WorkoutState {
  workouts: any[];
  isLoading: boolean;
  numberOfWorkouts: number;
  fetchWorkouts: (id: string, accessToken: string, tokenType: string) => Promise<void>;
  postWorkout: (workout: any, accessToken: string, tokenType: string) => Promise<void>;
  deleteWorkout: (workoutId: string, accessToken: string, tokenType: string) => Promise<void>;
}

const useWorkoutStore = create<WorkoutState>((set, get) => ({
  workouts: [],
  isLoading: true,
  numberOfWorkouts: 0,
  fetchWorkouts: async (id, accessToken, tokenType) => {
    set({ isLoading: true });
    try {
      const data = await getUserWorkoutData(id, accessToken, tokenType);
      set({ workouts: data, isLoading: false });
    } catch (error) {
      console.error("Error fetching workout data:", error);
      set({ isLoading: false });
    }
  },
  postWorkout: async (workout, accessToken, tokenType) => {
    try {
      await postWorkoutData(workout, accessToken, tokenType);
      set((state) => {
        const newWorkouts = [workout, ...state.workouts];
        return {
          workouts: newWorkouts,
          numberOfWorkouts: state.numberOfWorkouts + 1,
        };
      });
    } catch (error) {
      console.error("Error posting workout data:", error);
      throw error;
    }
  },
  deleteWorkout: async (workoutId, accessToken, tokenType) => {
    try {
      await deleteWorkoutData(workoutId, accessToken, tokenType);
      set((state) => {
        const filteredWorkouts = state.workouts.filter((workout) => workout.id !== workoutId);
        return {
          workouts: filteredWorkouts,
        };
      });
    } catch (error) {
      console.error("Error deleting workout data:", error);
      throw error;
    }
  },
}));

export default useWorkoutStore;
