import React, { useState } from "react";
import { StyleSheet, Button, TextInput } from "react-native";
import { Text, View } from "@/components/Themed";
import { useAuth } from "@/context/auth";
import { Link } from "expo-router"; 

export default function LoginScreen() {
  const auth = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSignIn = () => {
    auth?.signIn(username, password);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <View
        style={styles.separator}
        lightColor="#eee"
        darkColor="rgba(255,255,255,0.1)"
      />
      <TextInput
        style={styles.input}
        placeholder="Username"
        placeholderTextColor="black"
        onChangeText={setUsername}
        value={username}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        placeholderTextColor="black"
        onChangeText={setPassword}
        value={password}
        secureTextEntry={true}
      />
      <Button title="Sign-in" color={"orange"} onPress={handleSignIn} />
      <Link href="/register">
        <Text style={styles.registerText}>Register</Text>
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
  input: {
    backgroundColor: "white",
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
    width: "80%",
    textAlign: "center",
  },
  registerText: {
    color: "blue",
    marginTop: 20,
  },
});
