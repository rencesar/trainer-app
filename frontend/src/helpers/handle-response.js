import { authenticationService } from '../services/authService';

export function handleResponse(response) {
    return response
        .then(res => res.json())
        .then(data => {
            if (!response.ok) {
                if ([401, 403].indexOf(response.status) !== -1) {
                    // auto logout if 401 Unauthorized or 403 Forbidden response returned from api
                    authenticationService.logout();
                    window.location && window.location.reload(true);
                }

                const error = data.message || response.statusText;
                return Promise.reject(error);
            }

            return data;
        });
}