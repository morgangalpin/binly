import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '@angular/material';
import { SocketService } from '../shared';

import { SteeringComponent } from './steering.component';
import { SteeringService } from './steering.service';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule
  ],
  declarations: [SteeringComponent],
  exports: [SteeringComponent],
  providers: [SteeringService, SocketService]
})
export class SteeringModule { }
