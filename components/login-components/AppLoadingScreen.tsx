import React from "react";
import { Text, View, ActivityIndicator } from "react-native";
import { StyleSheet } from "react-native";

const AppLoadingScreen = () => {
  return (
    <View style={styles.container}>
      <ActivityIndicator size="large" color="#0000ff" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});

export default AppLoadingScreen;
