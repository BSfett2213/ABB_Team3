import { Routes } from '@angular/router';
import { UploadComponent } from './pages/upload/upload.component';
import { DateRangesComponent } from './pages/date-ranges/date-ranges.component';
import { TrainingComponent } from './pages/training/training.component';
import { SimulationComponent } from './pages/simulation/simulation.component';

export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'upload' },
  { path: 'upload', component: UploadComponent },
  { path: 'date-ranges', component: DateRangesComponent },
  { path: 'train', component: TrainingComponent },
  { path: 'simulation', component: SimulationComponent },
  { path: '**', redirectTo: 'upload' }
];
