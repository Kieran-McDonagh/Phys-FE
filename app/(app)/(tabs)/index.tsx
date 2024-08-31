import { useEffect } from "react";
import { StyleSheet, ScrollView } from "react-native";
import { Text, View } from "@/components/Themed";
import AllWorkouts from "@/components/workout-components/AllWorkouts";
import useWorkoutStore from "@/store/workoutStore";
import React from "react";
import useUserStore from "@/store/userStore";

export default function WorkoutScreen() {
  const { user } = useUserStore();
  const { workouts, isLoading, fetchWorkouts, numberOfWorkouts } = useWorkoutStore();

  useEffect(() => {
    if (user) {
      const { user_data, access_token, token_type } = user;
      fetchWorkouts(user_data.id, access_token, token_type);
    }
  }, [numberOfWorkouts]);

  if (workouts.length === 0 && !isLoading) {
    return <Text>No Workouts Found</Text>;
  }

  return (
    <View style={styles.container}>
      <ScrollView>
        <View>{isLoading ? <Text>Loading...</Text> : <AllWorkouts allWorkouts={workouts} />}</View>
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
});
