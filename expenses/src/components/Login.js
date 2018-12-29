import React, { Component } from 'react';
import { View, Text, Button, TextInput } from 'react-native';


class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
    };
    this.onUsernameChange = this.onUsernameChange.bind(this);
    this.onPasswordChange = this.onPasswordChange.bind(this);
  }

  onUsernameChange(username) {
    this.setState({username});
  }

  onPasswordChange(password) {
    this.setState({password})
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
        <Button onPress={() => this.props.navigation.navigate('ExpensesScreen')} title='Login' />
        <Button onPress={() => this.props.navigation.navigate('SignUpScreen')} title='SignUp' />
      </View>
    );
  }
}

export default Login;
