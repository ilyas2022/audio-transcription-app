import React, { useState, useEffect } from 'react';
import { AppBar, Toolbar, Typography, Button, Container, Box, Paper } from '@mui/material';
import { styled } from '@mui/material/styles';

const MainContainer = styled(Container)(({ theme }) => ({
  marginTop: theme.spacing(4),
}));

const App = () => {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    // Fetch message from backend server
    fetch('http://localhost:3000/')
      .then(response => response.text())
      .then(data => setMessage(data))
      .catch(error => {
        console.error('Error fetching data:', error);
        setMessage('Error connecting to server');
      });
  }, []);

  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Audio Transcription App</Typography>
        </Toolbar>
      </AppBar>
      <MainContainer>
        <Box mt={4}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>
              Welcome to Audio Transcription App
            </Typography>
            <Typography variant="body1">
              Server says: {message}
            </Typography>
            <Box mt={2}>
              <Button variant="contained" color="primary">
                Start Recording (Coming Soon)
              </Button>
            </Box>
          </Paper>
        </Box>
      </MainContainer>
    </div>
  );
};

export default App;