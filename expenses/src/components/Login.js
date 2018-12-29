import React, { Component } from 'react';
import { View, Text, Button, TextInput } from 'react-native';
import axios from 'axios';


class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
    };
    this.onUsernameChange = this.onUsernameChange.bind(this);
    this.onPasswordChange = this.onPasswordChange.bind(this);
    this.handleLogin = this.handleLogin.bind(this);
  }

  onUsernameChange(username) {
    this.setState({username});
  }

  onPasswordChange(password) {
    this.setState({password})
  }

  handleLogin() {
    const endpoint = '/auth/login/';
    const payload = { username: this.state.username, password: this.state.password }

    axios
      .post(endpoint, payload)
      .then(response => {
        const { token, user } = response.data;

        // set the returned token as the default auth header
        axios.defaults.headers.common.Authorization = `Token ${token}`;

        this.props.navigation.navigate('ExpensesScreen');
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <View>
        <TextInput
          placeholder="username"
          onChangeText={this.onUsernameChange}
        />
        <TextInput
          placeholder="password"
          secureTextEntry={true}
          onChangeText={this.onPasswordChange}
        />
        <Button onPress={this.handleLogin} title='Login' />
        <Button onPress={() => this.props.navigation.navigate('SignUpScreen')} title='SignUp' />
      </View>
    );
  }
}

export default Login;
