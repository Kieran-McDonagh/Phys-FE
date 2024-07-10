import React, { useState } from "react";
import { StyleSheet, Button, TextInput, TouchableOpacity } from "react-native";
import { Text, View } from "@/components/Themed";
import { useAuth } from "@/context/auth";
import { router } from "expo-router";
import MissingLoginData from "@/components/login-components/MissingLoginData";

export default function LoginScreen() {
  const auth = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [missingField, setMissingField] = useState<string | null>(null);

  const handleSignIn = () => {
    if (!username || !password) {
      setMissingField("Missing Field");
      return;
    }
    auth?.signIn(username, password);
  };

  const handleRegisterPress = () => {
    setMissingField(null);
    router.push("/register");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <TextInput
        style={styles.input}
        placeholder="Username"
        placeholderTextColor="black"
        onChangeText={setUsername}
        value={username}
        autoCapitalize='none'
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        placeholderTextColor="black"
        onChangeText={setPassword}
        value={password}
        secureTextEntry={true}
        autoCapitalize='none'
      />
      <TouchableOpacity onPress={handleSignIn}>
        <Text style={styles.signInText}>Log-in</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={handleRegisterPress}>
        <Text style={styles.registerText}>Register</Text>
      </TouchableOpacity>
      {missingField && <MissingLoginData message={missingField} />}
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
    fontSize: 30,
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
  signInText: {
    color: "orange",
    fontSize: 20,
    marginTop: 20,
  },
  registerText: {
    color: "blue",
    fontSize: 20,
    marginTop: 20,
  },
});
