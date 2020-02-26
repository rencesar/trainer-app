import React from "react";
import {Route, Switch} from "react-router-dom";
import Home from './app/Home'

const AppRoutes = ({ match }) => (
    <Switch>
        <Route path={`${match.url}home`} component={Home} />
    </Switch>
);

export default AppRoutes;