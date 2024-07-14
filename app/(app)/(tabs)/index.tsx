import { useEffect } from "react";
import { StyleSheet, ScrollView } from "react-native";
import { Text, View } from "@/components/Themed";
import { useAuth } from "@/context/auth";
import AllWorkouts from "@/components/workout-components/AllWorkouts";
import useWorkoutStore from "@/store/workoutStore";
import React from "react";

export default function WorkoutScreen() {
  const auth = useAuth();
  const { workouts, isLoading, fetchWorkouts, workoutPosted } =
    useWorkoutStore();

  useEffect(() => {
    if (auth && auth.user) {
      const { user } = auth;
      fetchWorkouts(user.user_data.id, user.access_token, user.token_type);
    }
  }, [workoutPosted]);

  if (workouts.length === 0 && !isLoading) {
    return <Text>No Workouts Found</Text>;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Workouts home page</Text>
      <View
        style={styles.separator}
        lightColor="#eee"
        darkColor="rgba(255,255,255,0.1)"
      />
      <ScrollView>
        <View>
          {isLoading ? (
            <Text>Loading...</Text>
          ) : (
            <AllWorkouts allWorkouts={workouts} />
          )}
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
