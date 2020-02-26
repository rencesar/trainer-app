import React from 'react';
import { Switch, Route, Redirect, useRouteMatch } from 'react-router-dom';
import Login from './Public/Login';
import Register from './Public/Register';
import ForgotPassword from './Public/ForgotPassword';
import AppRoutes from './Auth/AppRoutes';
import { authenticationService } from './services/authService';

const RestrictedRoute = ({ component: Component, ...rest }) =>
  <Route
    {...rest}
    render={props =>
      authenticationService.currentUserValue ?
        <Component {...props} />
        : <Redirect to={{ pathname: '/login', state: { from: props.location } }} />
    }
  />

function App() {
  let match = useRouteMatch();
  return (
    <Switch>
      <Route path="/login">
        <Login />
      </Route>
      <Route path="/register">
        <Register />
      </Route>
      <Route path="/forgot-password">
        <ForgotPassword />
      </Route>

      <RestrictedRoute path={`${match.url}`} component={AppRoutes} />
    </Switch>

  );
}

export default App;
