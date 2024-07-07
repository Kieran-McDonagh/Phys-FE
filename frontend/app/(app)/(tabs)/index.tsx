import { useState, useCallback, useEffect } from "react";
import { StyleSheet, ScrollView } from "react-native";
import { Text, View } from "@/components/Themed";
import { useAuth } from "@/context/auth";
import getUserWorkoutData from "@/api/workout-data";
import AllWorkouts from "@/components/workout-components/AllWorkouts";

export default function WorkoutScreen() {
  const auth = useAuth();
  const [workoutData, setWorkoutData] = useState<any[] | null>(null);

  const fetchData = async () => {
    if (auth && auth.user) {
      const { user } = auth;
      const id = user.user_data.id;
      const access_token = user.access_token;
      const token_type = user.token_type;
      try {
        console.log("fetching workout data");
        const data = await getUserWorkoutData(id, access_token, token_type);
        setWorkoutData(data);
      } catch (error) {
        console.error("Error fetching workout data:", error);
      }
    }
  };

  // TODO: call useeffect when workout is posted in modal
  useEffect(() => {
    fetchData();
  }, []);

  if (!workoutData) {
    return <Text>Loading workouts...</Text>;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Workouts home page</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <ScrollView>
        <View>
          <AllWorkouts allWorkouts={workoutData} />
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    padding: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 16,
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
});
