'use client';

import React from 'react';
import WeatherToolOutput from './WeatherTool';
import DealershipAddressToolOutput from './DealershipAddressTool';
import AppointmentAvailabilityToolOutput from './AppointmentAvailabilityTool';
import AppointmentConfirmationToolOutput from './AppointmentConfirmationTool';

interface ToolOutput {
  name: string;
  output: string;
}

// Tool Output Container that renders the appropriate component based on the tool name
export const ToolOutputContainer = ({ data }: { data: ToolOutput }) => {
  switch (data.name) {
    case 'get_weather':
      return <WeatherToolOutput data={data} />;
    case 'get_dealership_address':
      return <DealershipAddressToolOutput data={data} />;
    case 'check_appointment_availability':
      return <AppointmentAvailabilityToolOutput data={data} />;
    case 'schedule_appointment':
      return <AppointmentConfirmationToolOutput data={data} />;
    default:
      return null;
  }
};