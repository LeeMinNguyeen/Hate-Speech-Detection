export function get_uuid(url) {
    try {
        const response = fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = response.json();
        return result.UUID; // Assuming the response contains a `uuid` field
    } catch (error) {
        console.error('Error fetching UUID:', error);
        throw error;
    }
}